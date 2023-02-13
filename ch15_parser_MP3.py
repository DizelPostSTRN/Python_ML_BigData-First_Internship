class NotMP3Error(Exception):
    pass


class VersionError(Exception):
    pass


def parse_id3v2(filename: str = "") -> list:
    encodings = {
        0: 'ISO-8859-1',
        1: 'UTF-16',
        2: 'UTF-16BE',
        3: 'UTF-8'
    }
    result = []  # Список, в который будут записаны кортежи с данными
    try:
        with open(filename, "rb") as file:
            id3_data = file.read(10)
            file_id = id3_data[:3]  # Получаем идентификатор файла (ID3)
            if file_id != b'ID3':
                raise NotMP3Error("File {} not MP3".format(filename))  # Если файл не начинается с идентификатора ID3
            id3_ver = id3_data[3]  # Версия ID3v2
            if id3_ver not in (3, 4):
                raise VersionError("ID3V2 version of file {} not 3 or 4".format(filename))  # Если версия не 3 и не 4
            id3_s_bytes = id3_data[6:10]  # Размер данных в байтовой записи
            # Переводим в int
            id3_size = (id3_s_bytes[0] << 21) + (id3_s_bytes[1] << 14) + (id3_s_bytes[2] << 7) + id3_s_bytes[3]
            while file.tell() < 10 + id3_size:
                frame = file.read(10)
                frame_id = frame[:4]  # Идентификатор кадра
                if frame_id == b'\x00\x00\x00\x00':  # Если идентификатора нет пропускаем итерацию
                    break
                if id3_ver == 3:  # Размер данных для версии 3
                    frame_size = int.from_bytes(frame[4:8], 'big')
                elif id3_ver == 4:  # Размер данных для версии 4
                    frame_s_b = frame[4:8]
                    frame_size = (frame_s_b[0] << 21) + (frame_s_b[1] << 14) + (frame_s_b[2] << 7) + frame_s_b[3]
                frame_data = file.read(frame_size)  # Данные кадра
                frame_text_data = None
                if chr(frame_id[0]) == 'T':  # Если идентификатор начинается с T, пытаемся преобразовать в текст
                    if frame_data[0] in encodings.keys():
                        frame_text_data = frame_data[1:].decode(encodings[frame_data[0]])
                result.append(
                    (
                        frame_id,
                        frame_size,
                        frame_data,
                        frame_text_data
                    )
                )  # Добавляем кортеж в список
    except (IOError, NotMP3Error, VersionError) as e:
        print("{}: {}".format(e.__class__.__name__, e))
        return []
    return result


print(parse_id3v2("song.mp3"))

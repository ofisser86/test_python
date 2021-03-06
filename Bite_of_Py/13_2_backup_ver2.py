import os
import time


source = ['/home/didi/PycharmProjects/test_python/Bite_of_Py', '/home/didi/PycharmProjects/test_python/checkio']

target_dir = '/home/didi/PycharmProjects/test_python/Bite_of_Py/Backup'

today = target_dir+os.sep+time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today) # создание каталога
    print('Каталог успешно создан', today)

target = today + os.sep + now + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
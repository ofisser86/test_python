import os
import time


source = ['/home/didi/PycharmProjects/test_python/Bite_of_Py', '/home/didi/PycharmProjects/test_python/checkio']

target_dir = '/home/didi/PycharmProjects/test_python/Bite_of_Py/Backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
print(zip_command)
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')

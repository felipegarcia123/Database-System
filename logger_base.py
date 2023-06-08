import logging as log

log.basicConfig(level=log.DEBUG,
                format= '%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s]: %(message)s',
                datefmt='%I:%M:%S %p',
                handlers= [
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])


if __name__ == '__main__':
    log.debug('MENSAJE  ANIVEL DE DEBUG')
    log.info('MENSAJE A NIVEL DE INF')
    log.error('MESNSAJE A NIVEL DE ERROR')
    log.critical('MENSAJE A NIVEL DE CRITICAL')
    log.warning('MENSAJE A NIVEL DE WARNING')
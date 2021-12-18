import time

def run():

    with open('CPdescarga.txt','r', encoding='utf-8', errors='ignore') as f:

        for element in f.readlines():
            # d_codigo	d_asenta	d_tipo_asenta	D_mnpio	d_estado	d_ciudad	d_CP	c_estado	c_oficina	c_CP	c_tipo_asenta	c_mnpio	id_asenta_cpcons	d_zona	c_cve_ciudad
            print(element, end='')
            time.sleep(1)

if __name__ == '__main__':
    run()

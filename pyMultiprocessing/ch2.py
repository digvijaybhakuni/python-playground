from concurrent.futures  import ThreadPoolExecutor

def excute_with_state(num, share):
    print('share : {} num: {}'.format(share, num))
    return num ** num


with ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(excute_with_state, x, 'DIGGU') for x in range(100)]
    for f in futures:
        try:
            data = f.result()
        except Exception as exc:
            print('generated an exception: %s' % (exc))
        else:
            print('%d num pow' % (data))
        print(data)
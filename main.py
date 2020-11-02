from jsonio import JsonUtil
from submit import BondChain

if __name__ == "__main__":
    # convert data to json
    src_txt = 'test/1.txt'  # generated by Tencent QQ
    dst_json = 'test/1.json'
    JsonUtil.convert_txt_to_json(src_txt, dst_json)
    # initialize
    bc = BondChain()
    # login
    bc.login()
    # load data
    data = JsonUtil.load(dst_json)
    # traverse data and submit them
    failed = bc.submit_offers(data)
    # print failed offers
    if failed: print(f'\n* Totally {len(failed)} fail(s):')
    for fail in failed:
        print(fail)

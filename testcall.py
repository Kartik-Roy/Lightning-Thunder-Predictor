from pprint import pprint
import requests

sid = 'student580'
token = 'edc82e540212f12b53c661755600bbc2d79d5a96'
url = 'http://13.127.181.8:8000/get-audio-demo'



def connect_customer(sid, token,
                     customer_no, exotel_no, callerid, url,
                     timelimit=None, timeout=None,calltype="trans",
                     callback_url=None):
    return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Calls/connect.json'.format(sid=sid),

auth =(sid, token),
data = {'From': customer_no,
        'To': exotel_no,
        'CallerId': callerid,
        'Url': url,
        'TimeLimit': timelimit,
        'TimeOut': timeout,
        'CallType': calltype,
        'StatusCallback': callback_url})


if __name__ == '__main__':
    r = connect_customer(
        sid, token,
        exotel_no="08047103685",
        callerid="08047103685",
        url="http://my.exotel.in/exoml/start_voice/214054",
        timelimit="15",
        timeout="15",
        )
    print(r.status_code)
    pprint(r.json())

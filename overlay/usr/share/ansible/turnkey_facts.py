#!/usr/bin/python

DOCUMENTATION = '''
---
module: turnkey_facts
short_description: Gathers facts from TurnKey GNU/Linux Appliances
description:
    - Runs 'turnkey-version'
    - Returns:
        - turnkey                = True if successful
        - turnkey_app            = TurnKey Appliance application eg. wordpress
        - turnkey_ver            = TurnKey GNU/Linux version eg. 14.0
        - turnkey_arch           = Linux target architecture
        - turnkey_deb            = Codename for Debian version eg. jessie
        - turnkey_version_output = Output from turnkey-version
'''

import json
import subprocess

def is_number(s):
	try:
		float(s)
		return True
	except:
		return False

def main():
  turnkey_box = False
  result = { 'ansible_facts': {} }
  global module
  module = AnsibleModule(
    argument_spec       = dict(),
    supports_check_mode = True
  )

  try:
	rc = subprocess.check_output(["turnkey-version"]).rstrip()
	turnkey_box = True
  except:
	#could uncomment this line for testing if needed.
	#rc = "turnkey-jenkins-13.0-wheezy-amd64"
	turnkey_box = False

  if turnkey_box:
	facts = rc.split("-")

	#Get the version number. should be the only number in the facts list
	ver_list = filter(is_number, facts)
	if len(ver_list) == 1:
		ver_index = facts.index(ver_list[0])
	fact_version = ""
	#could be longer than the one number i.e. 14.0 RC2
	for i in facts[ver_index:len(facts)-2]:
		fact_version += i

	#application name should be from index 1 to version number index
	fact_app = ""
	for j in facts[1:ver_index]:
		fact_app += j+' '

	fact_arch = facts[-1]
	fact_deb = facts[-2]

  	result['ansible_facts']['turnkey'] = turnkey_box
  	result['ansible_facts']['turnkey_version_output'] = rc
  	result['ansible_facts']['turnkey_app'] = fact_app
  	result['ansible_facts']['turnkey_ver'] = fact_version
  	result['ansible_facts']['turnkey_arch'] = fact_arch
  	result['ansible_facts']['turnkey_deb'] = fact_deb
  else:
  	result['ansible_facts']['turnkey'] = turnkey_box

  module.exit_json(**result)

from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

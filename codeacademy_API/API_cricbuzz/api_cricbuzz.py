import requests
import xml.etree.ElementTree as ET 
import time


def get_url(url):
	response=requests.get(url)
	head=response.headers
	data=response.text
	return data


def matches_today(xml_data):
	root=ET.fromstring(xml_data)
	#print "Number of Matches held today are " + root.attrib['NMchs']
	print "Matches which are going now or completed recently"
	for child in root:
		if(child.tag=="match"):
			print child.attrib['mchDesc']+" <======  ID  OF   THE   MATCH  =====>  " + child.attrib['id']
	return root


def match_watch(get_root,match_id):
	root=get_root
	Id=match_id
	#print Id
	#print type(Id)
	if (int(Id)<30000):
		for child in root:
			if (child.tag=="match"):
				if(child.attrib['id']==Id):
					return child
	else:
		print "Number which is less than 10000"
		Id=raw_input("Select the Match ID once again from above Description - ")
		return match_watch(root,Id)
		#This is to be done later

def get_match_details(second_root):
	child=second_root
	dic=child.attrib
	if 'type' in dic:
		print "MATCH TYPE: "+ child.attrib['type']+"\n"
	if 'mnum' in dic:
		print "MATCH NO:   "+ child.attrib['mnum']+"\n"
	if 'srs' in dic:
		print "SERIES:     "+ child.attrib['srs']+"\n"
	if 'grnd' in dic:
		print "VENUE:      "+ child.attrib['grnd']+":"+child.attrib['vcity']+":"+child.attrib['vcountry']+"\n"
	return child.attrib['type']


def get_odi_scores(second_root):
	child=second_root
	for childs in child:
		if (childs.tag=="mscr"):
			for m_child in childs:
				if(m_child.tag=="btTm"):
					print "Batting Team - "+m_child.attrib['sName']
					for a_child in m_child:
						print a_child.attrib['r']+" - "+a_child.attrib['wkts']+" in "+a_child.attrib['ovrs']
				elif(m_child.tag=="blgTm"):
					print "Bowling Team - "+m_child.attrib['sName']
					for a_child in m_child:
						print a_child.attrib['r']+" - "+a_child.attrib['wkts']+" in "+a_child.attrib['ovrs']
		elif (childs.tag=="state"):
			if(childs.attrib['mchState']=="inprogress"):
				print childs.attrib['status']
				return "inprogress"
			else:
				print childs.attrib['status']
				return "complete"
				break

def get_t20_scores(second_root):
	child=second_root
	for childs in child:
		if (childs.tag=="mscr"):
			for m_child in childs:
				if(m_child.tag=="btTm"):
					print "Batting Team - "+m_child.attrib['sName']
					for a_child in m_child:
						print a_child.attrib['r']+" - "+a_child.attrib['wkts']+" in "+a_child.attrib['ovrs']
				elif(m_child.tag=="blgTm"):
					print "Bowling Team - "+m_child.attrib['sName']
					for a_child in m_child:
						print a_child.attrib['r']+" - "+a_child.attrib['wkts']+" in "+a_child.attrib['ovrs']
		elif (childs.tag=="state"):
			if(childs.attrib['mchState']=="inprogress"):
				print childs.attrib['status']
				return "inprogress"
			else:
				print childs.attrib['status']
				return "complete"
				break
		
def get_test_scores(second_root):#has to change this quite a bit data not available at present
	child=second_root
	for childs in child:
		if (childs.tag=="mscr"):
			for m_child in childs:
				if(m_child.tag=="btTm"):
					print "Batting Team - "+m_child.attrib['sName']
					for a_child in m_child:
						print a_child.attrib['r']+" - "+a_child.attrib['wkts']+" in "+a_child.attrib['ovrs']
				elif(m_child.tag=="blgTm"):
					print "Bowling Team - "+m_child.attrib['sName']
					for a_child in m_child:
						print a_child.attrib['r']+" - "+a_child.attrib['wkts']+" in "+a_child.attrib['ovrs']
		elif (childs.tag=="state"):
			if(childs.attrib['mchState']=="inprogress"):
				print childs.attrib['status']
			else:
				print childs.attrib['status']
				break



url="http://synd.cricbuzz.com/j2me/1.0/livematches.xml"
xml_data=get_url(url)
got_root=matches_today(xml_data)
match_id=raw_input("Select the Match ID from above Description - ")
second_root=match_watch(got_root,match_id)
typo=get_match_details(second_root)

if(typo=="TEST"):
	s=get_test_scores(second_root)
	while(s=='inprogress'):
		time.sleep(300)
		s=get_test_scores(second_root)
elif(typo=="ODI"):
	s=get_odi_scores(second_root)
	while(s=='inprogress'):
		time.sleep(300)
		s=get_odi_scores(second_root)
else:
	s=get_t20_scores(second_root)
	while(s=='inprogress'):
		time.sleep(300)
		s=get_t20_scores(second_root)





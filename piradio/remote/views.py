import json
from subprocess import *
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
def main_page(request):
	msg = runCmd("mpc current").strip()
	playlist = runCmd("mpc playlist")
	playlist = playlist.strip().split("\n")
	items = []
	for idx, val in enumerate(playlist) :
		items.append( {'id' : idx+1, 'url' : val} )

	url = 'remote/index.html'
	model = {'current' : msg,
			'volume' : get_volume(),
			'playlist' : items}
	return render_to_response(url, model)

def seek(request, no):
	
	return process("mpc play " + no)

def get_volume():
	volume = runCmd("mpc status | grep volume")
	volume = volume[7:volume.find("%")+1]

	return volume

def stop(request):
	
	return process("mpc stop")


def volumeUp(request):
	
	return process("mpc volume +5")


def volumeDown(request):
	return process("mpc volume -5")

def process(cmd) :
		
	msg = runCmd(cmd)
	msg = runCmd("mpc current")

	result = {}
	result['current'] = msg
	result['volume'] = get_volume()
	return HttpResponse(json.dumps(result), content_type="application/json")



def runCmd(cmd) :
	p = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
	output = p.communicate()[0]
	return output

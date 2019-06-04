import json
import requests
import time
import datetime
import math

def _convert_size(size_bytes):
	'''
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   '''
	s = math.ceil(size_bytes / 1024)
	return s
	#return "%s %s" % (s, size_name[i])

def _formatTime(timeData):
	hours, remainder = divmod(timeData, 3600)
	minutes, seconds = divmod(remainder, 60)
	return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
	
def _formatDimensions(d,h,w):
	return "{0} x {1} x {2}".format(round(d,2),round(h,2),round(w,2))

def _buildFileLogs(files):
	report = []
	rowDataHeadings = [
		'File Name',
		'Date',
		'File Size (mega bytes)',
		'Dimensions',
		'Failed Prints',
		'Successful Prints',
		'Average Print Time',
		'Last Print Time',
		'Estimated Print Time'
	]

	report.append(rowDataHeadings)
	
	for file in files:
		rowData = []
		rowData.append(file['display'])
		
		ts = file['date']
		localTime = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(ts))
		rowData.append(localTime)
		
		rowData.append(_convert_size(file['size']))
		
		if 'gcodeAnalysis' in file:
			if 'dimensions' in file['gcodeAnalysis']:
				dimension = file['gcodeAnalysis']['dimensions']
				dimensions = _formatDimensions(dimension['depth'],dimension['height'],dimension['width'])
				
		rowData.append(dimensions)
		
		if 'prints' in file:
			if 'failure' in file['prints']:
				rowData.append(file['prints']['failure'])
			else:
				rowData.append("---")
				
			if 'success' in file['prints']:
				rowData.append(file['prints']['success'])
			else:
				rowData.append("---")
		else:
			rowData.append("---")
			rowData.append("---")
		
				
		if 'statistics' in file:
			if 'ender3' in file['statistics']['averagePrintTime']:
				timeData = file['statistics']['averagePrintTime']['ender3']
				rowData.append(_formatTime(timeData))
			else:
				rowData.append("---")
			if 'ender3' in file['statistics']['lastPrintTime']:
				timeData = file['statistics']['lastPrintTime']['ender3']
				rowData.append(_formatTime(timeData))
			else:
				rowData.append("---")
		else:
				rowData.append("---")
				rowData.append("---")

		if 'gcodeAnalysis' in file:
			if 'estimatedPrintTime' in file['gcodeAnalysis']:
				timeData = file['gcodeAnalysis']['estimatedPrintTime']
				rowData.append(_formatTime(timeData))
		
		report.append(rowData)

	return report

def getOctoPrint_PrintLogs():
	#connect
	hostName = 'http://192.168.0.4'
	endPoint = '/api/files'#get file information
	#endPoint = '/api/files/local/please_dear_god.gcode'#get file information
	url = hostName + endPoint
	
	octoprintApiKey = open('octoprint-api-key','r').read()
	
	#local network only so this is safe to be public
	headers = {
			'Content-type': 'application/json',
			'X-Api-Key' : octoprintApiKey
			}
			
	paramList = {}#no parameters needed
	
	r = requests.get(url, headers=headers, params=paramList)
	r.raise_for_status()
	
	response = json.loads(r.text)
	
	#reports = _buildFileLogs(response['files'])
	return _buildFileLogs(response['files'])
	

'''
TESTS
'''	


'''
template = "{0} = {1}"
print(template.format('File',response['display']))

ts = response['date']

localTime = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(ts))
print(template.format('Date',localTime))

print(template.format('File Size',convert_size(response['size'])))

dimension = response['gcodeAnalysis']['dimensions']
dimensions = formatDimensions(dimension['depth'],dimension['height'],dimension['width'])
print(template.format('Print Dimensions',dimensions))

print(template.format('Failed Prints',response['prints']['failure']))
print(template.format('Successful Prints',response['prints']['success']))

timeData = response['statistics']['averagePrintTime']['ender3']
print(template.format('Average Print Time',formatTime(timeData)))

timeData = response['statistics']['lastPrintTime']['ender3']
print(template.format('Last Print Time',formatTime(timeData)))

timeData = response['gcodeAnalysis']['estimatedPrintTime']
print(template.format('Estimated Print Time',formatTime(timeData)))
'''

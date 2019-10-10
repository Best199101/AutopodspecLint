#! /usr/bin/python
# -*- coding: utf-8 -*-


import os, sys
import fileinput
import time



new_tag = raw_input('请输入项目更新版本号:')

pod_sources = 'https://github.com/jiexingtianxia/G_Hey_podSpecs.git'
git_sources = 'https://github.com/jiexingtianxia/G_OSLib.git'

project_name = 'G_Hey_podSpecs'
podspec_name = 'G_OSLib.podspec'

project_path = os.getcwd()

new_tag = new_tag.strip()
	
lib_cmd = ''
pod_push_cmd = ''
spec_file_path = project_path + "/" + podspec_name

def updateVersion():

  f = open(spec_file_path,'r+')
  infos = f.readlines()
  f.seek(0, 0)
  file_data = ""
  new_line = ""

  for line in infos:
    if line.find('s.version ') != -1:

      line = '  s.version          = \'%s\' \n' % new_tag

    elif line.find('s.source ') != -1:

      line = '  s.source           = { :git => \'%s\', :tag => \'%s\' } \n' % (git_sources,new_tag)

    else :

      print('==================')

    print('******************%s') % line

    file_data += line

  with open(spec_file_path, 'w', ) as f1:

    f1.write(file_data)

  f.close()

def podCmd():

	global lib_cmd
	global pod_push_cmd
	source_suffix = 'https://github.com/CocoaPods/Specs.git --allow-warnings'
	lib_cmd = 'pod lib lint --sources='
	lib_cmd += git_sources
	lib_cmd += ','
	lib_cmd += source_suffix

	pod_push_cmd = 'pod repo push ' + project_name + ' ' + podspec_name
	pod_push_cmd += ' --sources='
	pod_push_cmd += pod_sources
	pod_push_cmd += ','
	pod_push_cmd += source_suffix



def libLint():
    print('*****************waiting for pod lib lint checking 🍺 🍺 🍺')

    os.system(lib_cmd)

def gitPush():

    print('*****************waiting for git push 🍺 🍺 🍺')
    os.system('git add .')

    commit_desc = 'version_' + new_tag
    commit_cmd = 'git commit -m ' + commit_desc
    os.system(commit_cmd)
   
    r = os.popen('git symbolic-ref --short -q HEAD')
    current_branch = r.read()
    r.close()

    push_cmd = 'git push origin ' + current_branch
    tag_cmd = 'git tag ' + new_tag
    os.system(push_cmd)
    os.system(tag_cmd)
    os.system('git push --tags')

def podPush():
    print('*****************waiting for pod push 🍺 🍺 🍺')
    os.system(pod_push_cmd)


updateVersion()
podCmd()
libLint()
gitPush()
podPush()




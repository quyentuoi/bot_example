import shlex
import subprocess

# Tokenize the shell command
# cmd will contain  ["ping","-c1","google.com"]     
cmd=shlex.split("ping -c10 google.com")
try:
   print subprocess.check_output(cmd)

except subprocess.CalledProcessError,e:
   #Will print the command failed with its exit status
   print "The IP {0} is NotReacahble".format(cmd[-1])
else:
   print "The IP {0} is Reachable".format(cmd[-1])

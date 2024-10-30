param ( [Parameter(Mandatory=$true)][string]$user, $port )

Cls
Write-Host "`t`t`n ********** Connect To Imperial DoC Labs **********`n"

# Check if the port argument isn't supplied, default it to 14000
# Preferred ports range 10000-20000, See Documentations !!
 
if ($port -lt 1)
{
    $port = 14000

 }

# Use SSH Tunnelling with the additional Parameter -L to retrieve data between remote and local
#with the user name and port
ssh -t -L ${port}:localhost:$port $user@shell1.doc.ic.ac.uk "/vol/linux/bin/sshtolab -e /vol/lab/ml/intro2ml -g -w ~/ -p $port" 

# Additional confirmation that the user session is closed !
Write-Host "`nConnection for $user is now closed."

# Manifest to end a process
exec { 'pkill killmenow':
path    => ['/usr/bin', '/usr/sbin',]
}
#Manifest that execute command pkill to kill a command
exec { 'kill_process' :
    command => 'pkill killmenow',
    path    => '/usr/bin',
}

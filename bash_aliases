# ~/.bash_aliases
# Seperate file for bash aliases
# Sourced by ~/.bashrc

# Update dependencies and list upgradable packages.
alias aptup="echo \"sudo apt update && apt list --upgradable\" && sudo apt update && apt list --upgradable"

# Restart plasmashell (DE), probably in a bad way.
alias plasmarestart="killall plasmashell && sleep 3 && kstart5 plasmashell"

# Tjekker DBA.dk.
alias dba="~/Coding/bin/dba.py bastl monotron volca -category=musikinstrumenter/musikinstrumenter elektron"

# Remove backup files and vim undo files in current directory, but prompt user
# before each removal.
alias rmb="rm -i *~ ; rm -i .*~"

# If the file ./index.html does not exist, create a copy of
# ~/Coding/default-index.html called ./index.html
# Note: file as in anything (reg file, dir, symlink, node etc.), not just a regular file.
alias hsi="[[ ! -e ./index.html ]] && cp ~/Coding/default-index.html ./index.html"

# Usage: cl [dir]
# cd into [dir] and run ls.
function cl {
	if [ -z "$1" ]; then
		cd ~
		ls --color=auto -F
	elif [ -d "$1" ]; then
		cd "$1"
		ls --color=auto -F
	else
		echo "Usage: cl [dir]"
		echo "cd into directory and run ls"
	fi
}


# Usage: mkcd [dir]
# Create [dir] and cd into it
function mkcd {
	if [[ -z "$1" || $# > 1 ]]; then
		echo "Error: mkcd takes exactly one argument."
		echo "Usage: mkcd [dir]"
		echo "Create [dir] and cd into it"
	else
		mkdir "$1" && cd "$1"
	fi
}


# List 10 most used commands from .bash_history
function histstat {
	history | awk '{CMD[$2]++;count++;}END { for (a in CMD)print CMD[a] " " CMD[a]/count*100 "% " a;}' | grep -v "./" | column -c3 -s " " -t | sort -nr | nl |  head -n10
}

# temporary, fordi jeg sikkert glemmer at det hedder exec bash
alias reload="echo 'det hedder exec bash' ; exec bash"

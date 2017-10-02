" Config for ft=python

" Comment out selection with #
vnoremap <buffer> <Leader>c <Esc>'<<C-V>'><S-I>#<Esc>

" Comment out selection in """ block
vnoremap <buffer> <Leader>C <Esc>'<O"""<Esc>'>o"""<Esc>

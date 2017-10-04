" Config for ft=python

" Insert shebang line
nnoremap <buffer> <Leader>! mmggO#!/usr/bin/env python3<Esc>`m

" Comment out selection with #
vnoremap <buffer> <Leader>c <Esc>'<<C-V>'><S-I>#<Esc>

" Comment out selection in """ block
vnoremap <buffer> <Leader>C <Esc>'<O"""<Esc>'>o"""<Esc>

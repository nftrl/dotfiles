" Config for ft=sh

" Instert shebang line
nnoremap <buffer> <Leader>! mmggO#!/bin/bash<Esc>`m

" Comment out selection
vnoremap <buffer> <Leader>c <Esc>'<<C-V>'><S-I>#<Esc>

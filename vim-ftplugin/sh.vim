" Config for ft=sh

" Instert shebang line
"nnoremap <buffer> <Leader>! mmggO#!/bin/bash<Esc>`m
nnoremap <buffer> <Leader>! ggO#!/bin/bash<Esc><C-O>

" Comment out selection
" FIXME: It starts the comment block line in '<. If '< is further indented
" than some other lines, the bulk commenting is not done right, as the comment
" block will go through the less indented lines.
vnoremap <buffer> <Leader>c <Esc>'<<C-V>'><S-I>#<Esc>

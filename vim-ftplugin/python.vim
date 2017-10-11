" Config for ft=python

" Insert shebang line
nnoremap <buffer> <Leader>! mmggO#!/usr/bin/env python3<Esc>`m

" Comment out selection with #
" FIXME: It starts the comment block line in '<. If '< is further indented
" than some other lines, the bulk commenting is not done right, as the comment
" block will go through the less indented lines.
vnoremap <buffer> <Leader>c <Esc>'<<C-V>'><S-I>#<Esc>

" Comment out selection in """ block
" FIXME: Not the best indentation.
vnoremap <buffer> <Leader>C <Esc>'<O"""<Esc>'>o"""<Esc>

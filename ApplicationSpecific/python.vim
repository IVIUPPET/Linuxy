set tabstop=8
set expandtab
set shiftwidth=4
set softtabstop=4

" [block comment mapping]
" map insertmode ctrl+c to substitute '#' at beginning of selected
" lines: 
" :s/^/# 
" then hit enter
vmap <C-c> :s/^/#<enter>

" also need so can just hit ctrl c while on a line in insert mode
" remove previous mapping in normal and insert, then remap
nnoremap <C-c> <Nop>
inoremap <C-c> <Nop>
nmap <C-c> :s/^/#<enter>
imap <C-c> <esc>:s/^/#<enter>


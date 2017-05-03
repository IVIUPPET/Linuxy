" LaTeX (rubber) macro for compiling
nnoremap <leader>c :w<CR>:!rubber --pdf --warn all %<CR>

" View PDF in mupdf macro; '%:r' is current file's root (base) name
nnoremap <leader>v :!mupdf %:r.pdf &<CR><CR>


" [block comment mapping]
" map insertmode ctrl+c to substitute '#' at beginning of selected
" lines: (well, % for tex)
" :s/^/# 
" then hit enter
vmap <C-c> :s/^/%<enter>

" also need so can just hit ctrl c while on a line in insert mode
" remove previous mapping in normal and insert, then remap
nnoremap <C-c> <Nop>
inoremap <C-c> <Nop>
nmap <C-c> :s/^/%<enter>
imap <C-c> <esc>:s/^/%<enter>


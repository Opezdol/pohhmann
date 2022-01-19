"this is a comment in vimrc


"lines longer than 79 will be broken (REITZ)
set textwidth=79 

" when using >> or << commands, shift lines by 4 spaces
set shiftwidth=4

"Set tabs to have 4 stops
set tabstop=4

" expand tabs into spaces
set expandtab

"insert/delete 4 spaces when hitting TAB/BACKSPACE
set softtabstop=4

" round indent to multiple of 'shiftwidth'
set shiftround

" indent when moving to the next line
set autoindent
" set visual line at cursor position 
set cursorline

" set numbering of lines
set number

" show mathcing part for {} [] ()
set showmatch

" enable all python syntax highlighting features
let python_highlight_all = 1

" turn off preview-bitch
set completeopt-=preview
syntax enable "enable syntax highlighting


"__________________________-
"Vundle plugin setup
set nocompatible
filetype off

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.

" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
"Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
" Plugin 'L9'
" Git plugin not hosted on GitHub
"Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
"Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
"Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plugin 'ascenator/L9', {'name': 'newL9'}


Plugin 'jnurmine/zenburn'
Plugin 'hhatto/autopep8'
Plugin 'valloric/youcompleteme'
Plugin 'flazz/vim-colorschemes'
Plugin 'tell-k/vim-autopep8'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

"___________________________-
"Vundle END
"
"remap Esc to jk combo, lets try it, everyone say it's more comfortable than hitESCAPE-button
inoremap jk <esc>
inoremap JK <esc>

"Automatic folding section
"set foldmethod=indent
set foldmethod=indent

"remap space to fold
nnoremap <space> za
colors molokai

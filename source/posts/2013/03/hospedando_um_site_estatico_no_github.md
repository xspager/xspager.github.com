Date: 2013-03-12
Title: Hospedando um site estático na sua conta do GitHub
Tags: github, pelican
status: draft

O primeiro passo é criar uma conta no GitHub se você ainda não tiver uma. Para criar uma conta grátis, vá em [https://github.com/signup/free]() e se cadastre-se.


Passos para criar a conta?

Agora precisamos criar um novo repositório git na sua conta que vai ser o site. O nome desse repositório deve seguir o padrão nome_do_seu_usuario.github.com
Passos pra criar o repositório?

Para poder começar a criar o seu site você vai ter que clonar o esse repositório na rua máquina local. Para quem não está familiarizado com git, você vai rodar:

    $ git clone

A seguir vamos criar um arquivo HTML(no caso HTML5) básico no estilo "Hello, World!". Crie um arquivo chamado index.html na raiz do clone do seu repositório com o código a seguir:

    <!DOCTYPE html>
    <html lang="en">
       <head>
           <meta charset="utf-8">
           <title>Hello World</title>
       </head>
       <body>
           <h1>Hello World</h1>
           <p>
               Hello, World!
           </p>
       </body>
    </html>

Commite o arquivo:

    $ git add index.html

E faça o push para o github:

    $ git push

Aguarde alguns minutos para que o github identifique que esse repositório é uma pagina e depois acesse nome_do_seu_usuario.github.com.
Indo um pouco além do HTML escrito a mão, podemos usar um gerador de sites estáticos como o [Pelican](http://docs.getpelican.com/) Com ele você pode escrever o seu site/blog em [Markdown](http://daringfireball.net/projects/markdown/), [reStructuredText](http://docutils.sourceforge.net/rst.html) ou [AsciiDoc](http://www.methods.co.nz/asciidoc/index.html)

Baseado no: [http://yakattack-steel-trap.blogspot.com.br/2012/04/hosting-your-html-on-github.html]()

(defpackage #:poll-example
  (:use #:cl #:hunchentoot #:risp))
  
(in-package #:poll-example)

;; Definição das opções da enquete
(defvar *options* (list (cons "JavaScript" 0)
                        (cons "Python" 0)
                        (cons "Java" 0)))

;; Página principal com a enquete
(define-route (index-page :uri "/")
  (with-html-output-to-string (*standard-output*)
    (:html
     (:head (:title "Sistema de Votação"))
     (:body
      (:h1 "Qual é sua linguagem de programação favorita?")
      (:form :method "post"
             (loop for (option . _) in *options*
                   do (html (:input :type "submit"
                                    :name "option"
                                    :value option))))
      (:h2 "Resultados:")
      (:ul
       (loop for (option votes) in *options*
             collect (:li (format nil "~a: ~a votos" option votes))))))))

;; Incrementa o voto para a opção selecionada
(defun vote (option)
  (setf (cdr (assoc option *options*)) (1+ (cdr (assoc option *options*)))))

;; Rota para processar o voto enviado pelo formulário
(define-route (vote-page :uri "/vote" :method :post)
  (let ((option (cdr (assoc "option" (parameters))))) 
    (vote option)
    (redirect "/")))

;; Inicia o servidor
(start (make-instance 'easy-acceptor :port 8080))

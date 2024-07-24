from lorem_text import lorem

def main(params):
     words = 10

     return {
          # specify headers for the HTTP response
          # we only set the Content-Type in this case, to 
          # ensure the text is properly displayed in the browser
          "headers": {
              "Content-Type": "text/plain;charset=utf-8",
          },
          
          ## use the text generator to create a response sentence
          #  with 10 words
          "body": lorem.words(words),
      }

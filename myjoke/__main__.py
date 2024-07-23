import pyjokes

def main(params):
     return {
          "headers": {
              "Content-Type": "application/json;charset=utf-8",
          },
          "body": {
               "joke":pyjokes.get_joke(),

               }
      }

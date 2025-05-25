from app import create_app

print("Starting Flask app...")  


app = create_app()

if __name__ == "__main__":
   print("Running app...")    
   app.run(host="0.0.0.0", port=5050)

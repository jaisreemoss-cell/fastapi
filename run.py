import webbrowser
import uvicorn

if __name__ == "__main__":
    # Automatically open http://127.0.0.1:8000/docs in your browser
    webbrowser.open("http://127.0.0.1:8000/docs")
    
    # Start the server
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
import logging

logging.basicConfig(level=logging.ERROR, filename='app_errors.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled error: {exc}")
    # Return the customized error response

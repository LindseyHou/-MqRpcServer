import uvicorn


def main() -> None:
    uvicorn.run("app:app", host="127.0.0.1", port=8091, reload=False)


if __name__ == "__main__":
    main()

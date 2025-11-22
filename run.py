from app.server import app, init_data

if __name__ == '__main__':
    print("Starting AlbumELO...")
    init_data()
    app.run(debug=True)

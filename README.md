<h2>MemeGen</h2>

Practice with Python, image, filesystem, CLI arguments, flask, etc..

Generates a "meme-like" image from either a set of random included dog pics, and random stupid quotes, or custom file and quote.

**app.py** : Flask version of the app. Run and connect to 127.0.0.1:5000

**meme.py** : Command-line version. With no arguments, generates image files from built-in data. Optional arguments --quote --author and --path
can be used to specify custom quote, author, and image file path.

<h3>Usage</h3>

Assumes python is installed. Copy repository to local directory. Verify packages in requirements.txt are available.

Run **python3 app.py** to start the web server.

Run **python3 meme.py** to generate a random meme, or with the -h option to see command line options.


<h3>Modules:</h3>

<h4>Quote processing</h4>

**quotemodel:** Object containing one quote

**quoteengine:** Abstract base class for all importer modules. Also implements class method can_ingest(file) which will distribute a file to appropriate child class for loading. Depends on ingestors below.

**csvingestor, docxingestor, pdfingestor, textingestor:** Parse files of respective types in to quote objects. Depends on above.

**importer:** Interface filesystem to quoteengines, walk directories and load, etc.. Depends on above.

<h4>Usage</h4>

If you are using these classes, it's probably to load quotes from various CSV files in known folders. Instantiate a new importer object with Importer(). Then call its parse_all() method, which will return a list of quote objects. You can then randomly choose a quote, or do whatever with them. You can also call parse_file(filepath: str) directly to load a single file and return a list of quotes.


<h4>Meme engine</h4>

**imagesizer:** Resizing of image as needed

**imagetexter:** Handles addition of text to the image

**memeengine:** Assembly of quote and image in to new, final image. Depends on two previous.

<h4>Usage</h4>

Instantiate a new engine with MemeEngine(outpath: str). All finished images will appear in the specified outpath folder. You can then call make_meme(img: str, body: str, author: str) which completely creates the meme image, and returns the path to the finished image.

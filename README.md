<h2>MemeGen</h2>

Practice with Python, image, filesystem, CLI arguments, flask, etc..

Generates a "meme-like" image from either a set of random included dog pics, and random stupid quotes, or custom file and quote.

**app.py** : Flask version of the app. Run and connect to 127.0.0.1:5000

**meme.py** : Command-line version. With no arguments, generates image files from built-in data. Optional arguments --quote --author and --path
can be used to specify custom quote, author, and image file path.

<h3>Modules:</h3>

<h4>Quote processing</h4>

**quotemodel:** Object containing one quote

**quoteengine:** Base class for all importer modules. Implements can_ingest(file) which will distribute a file to appropriate child class for loading.

**csvingestor, docxingestor, pdfingestor, textingestor:** Parse files of respective types in to quote objects.

**importer:** interface filesystem to quoteengines, walk directories and load, etc..


<h4>Meme engine</h4>

**imagesizer:** resizing of image as needed

**imagetexter:** handles addition of text to the image

**memeengine:** assembly of quote and image in to new, final image

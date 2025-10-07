from fastapi import FastAPI

app = FastAPI()

@app.get("/organisms")
def list_organisms():
    """Return a list of example organisms."""
    organisms = [
        "Escherichia coli",
        "Saccharomyces cerevisiae",
        "Drosophila melanogaster",
        "Caenorhabditis elegans",
        "Mus musculus",
        "Homo sapiens"
    ]
    return {"organisms": organisms}

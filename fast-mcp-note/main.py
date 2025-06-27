from fastmcp import FastMCP
import resources.notes as notes
mcp=FastMCP()


@mcp.tool
def createNote(content:str,title:str=None)->int:
 """create new note with title and content, title is optional"""
 return notes.createNote(content,title)


@mcp.resource(uri="/notes",description="notes resource")
def getNotes():
    """get all notes"""
    print("getNotes")
    return notes.getNotes()


if __name__=="__main__":
    mcp.run()



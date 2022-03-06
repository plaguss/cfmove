"""Script to track downloads of videos.
"""

import pathlib
from typing import List

from tinydb import Query, TinyDB

TRACK_PATH = pathlib.Path.cwd().parent / "track.json"


def register_video(
    url: str = None, title: str = None, name: str = None, movements: List[str] = None
) -> None:
    """Resume info of the video, to keep track of the work done.

    Parameters
    ----------
    url : str, optional
        URL of the downloaded video, by default None
    title : str, optional
        Title of the video in youtube, by default None
    name : str, optional
        Name of the athlete, by default None

    Examples
    --------
    >>> register_video(url=r"https://www.youtube.com/watch?v=4-5ZJahGp0o",
    ...     title="Friendly Fran - Online Semifinals Event 1",
    ...     name=r"Bryan Hernandez"
    ... )
    """
    with TinyDB(TRACK_PATH) as db:
        downloads = db.table("downloads")
        downloads.insert(
            {"url": url, "title": title, "name": name, "movements": movements}
        )

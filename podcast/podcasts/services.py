from typing import List, Iterable

from podcast.adapters.repository import AbstractRepository
from podcast.domainmodel.model import Podcast, Review, Category, Episode


# Functions to convert model entities to dicts

def get_number_of_podcasts(repo: AbstractRepository):
    return repo.get_number_of_podcasts()

def podcast_id(id, repo: AbstractRepository):
    podcasts = get_podcast_dicts(repo)
    return podcasts[id]

def get_podcast_dicts(repo: AbstractRepository):
    podcasts = repo.get_list_of_podcasts()
    podcast_dicts = {}

    for podcast in podcasts:
        podcast_dict = podcast_to_dict(podcast)
        podcast_dicts[podcast_dict["id"]] = podcast_dict
    return podcast_dicts


def podcast_to_dict(podcast: Podcast):
    podcast_dict = {
        'id': podcast.id,
        'author': podcast.author,
        'title': podcast.title,
        'image': podcast.image,
        'description': podcast.description,
        'website': podcast.website,
        'itunes_id': podcast.itunes_id,
        'language': podcast.language,
        'categories': categories_to_string(podcast.categories),     # Categories current unimplemented.
        'episodes': episodes_to_dict(podcast.episodes)
    }
    return podcast_dict


def category_to_dict(category: Category):
    category_dict = {
        'id': category.id,
        'name': category.name,
        'tagged_podcasts': [podcast.id for podcast in category.tagged_podcasts]
    }
    return category_dict


def categories_to_dict(categories: Iterable[Category]):
    return [category_to_dict(category) for category in categories]


def categories_to_string(categories):
    categories_list = categories_to_dict(categories)
    categories_string = " | ".join([category['name'] for category in categories_list])
    return categories_string


def episode_to_dict(episode: Episode):
    episode_dict = {
        'id': episode.id,
        'podcast_id': episode.podcast_id,
        'title': episode.title,
        'audio': episode.audio,
        'length': episode.length,
        'description': episode.description,
        'upload_date': episode.upload_date,
        'reviews': [review.id for review in episode.reviews]
    }
    return episode_dict


def episodes_to_dict(episodes: Iterable[Episode]):
    return [episode_to_dict(episode) for episode in episodes]

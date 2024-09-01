"""Initialize Flask app."""

from pathlib import Path
from flask import Flask, render_template

# TODO: Access to the podcast should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!

# Marked for deletion
from podcast.domainmodel.model import Podcast, Author
# ; This is to be taken care of by blueprints

import podcast.adapters.repository as repo
from podcast.adapters.memory_repository import MemoryRepository


# TODO: Access to the podcast should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!


def create_app():
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    data_path = Path('podcast') / 'adapters' / 'data'

    # Create the MemoryRepository implementation for a memory-based repository
    repo.repo_instance = MemoryRepository()
    # Fills the content of the repository from the provided csv files
    repo.repo_instance.populate(data_path)

    with app.app_context():
        # Register blueprints
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .podcasts import podcasts
        app.register_blueprint(podcasts.podcasts_blueprint)

        from .utilities import utilities
        app.register_blueprint(utilities.utilities_blueprint)

        # Finished further blueprints
        """
        @app.route('/podcasts')
        def podcasts():
            return render_template('podcasts.html', podcasts=podcasts)
        """
    return app

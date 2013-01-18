from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.api import (bind_links,
    register_model_list_columns)
from common.utils import encapsulate
from project_setup.api import register_setup
from documents.permissions import (PERMISSION_DOCUMENT_NEW_VERSION, 
    PERMISSION_DOCUMENT_CREATE)
from documents.models import Document

from .staging import StagingFile
from .models import (WebForm, StagingFolder, WatchFolder)
from .widgets import staging_file_thumbnail
from .links import (staging_file_delete, setup_sources,
    setup_web_form_list, setup_staging_folder_list, setup_watch_folder_list,
    setup_source_edit, setup_source_delete, setup_web_form_create, setup_staging_folder_create,
    source_transformation_list, upload_version,
    document_create_multiple, document_create_siblings)

bind_links([StagingFile], [staging_file_delete])

bind_links(['setup_web_form_list', 'setup_staging_folder_list', 'setup_watch_folder_list', 'setup_source_create', 'setup_source_create_staging_folder', 'setup_source_create_web_form'], [setup_web_form_list, setup_staging_folder_list], menu_name='form_header')

bind_links([WebForm], [setup_web_form_list, setup_staging_folder_list], menu_name='form_header')
bind_links([WebForm], [source_transformation_list, setup_source_edit, setup_source_delete])

bind_links([WebForm, 'setup_web_form_list', 'setup_source_create_web_form'], [setup_web_form_create], menu_name='secondary_menu')
bind_links([StagingFolder, 'setup_staging_folder_list', 'setup_source_create_staging_folder'], [setup_staging_folder_create], menu_name='secondary_menu')

bind_links([StagingFolder], [setup_web_form_list, setup_staging_folder_list], menu_name='form_header')
bind_links([StagingFolder], [source_transformation_list, setup_source_edit, setup_source_delete])

bind_links([WatchFolder], [setup_web_form_list, setup_staging_folder_list, setup_watch_folder_list], menu_name='form_header')
bind_links([WatchFolder], [source_transformation_list, setup_source_edit, setup_source_delete])

# Document version
bind_links(['document_version_list', 'upload_version', 'document_version_revert'], [upload_version], menu_name='sidebar')

bind_links(['document_list_recent', 'document_list', 'document_create', 'upload_interactive', 'staging_file_delete', 'document_create_multiple'], [document_create_multiple], menu_name='secondary_menu')

bind_links([Document], document_create_multiple, menu_name='secondary_menu')
bind_links([Document], document_create_siblings)

register_model_list_columns(StagingFile, [
        {'name':_(u'thumbnail'), 'attribute':
            encapsulate(lambda x: staging_file_thumbnail(x))
        },
    ])

register_setup(setup_sources)

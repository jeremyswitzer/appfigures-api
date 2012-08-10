from base import BaseClient

ARCHIVE_BASE_URI = "archive"
ALL_REPORTS = None
LATEST_REPORTS = "latest"

class ArchiveClient(BaseClient):

    def __init__(self, result_service, uri=ARCHIVE_BASE_URI):
        super(ArchiveClient, self).__init__(uri, result_service)
        
    def get_archive(self, scope, report_type):
        args = (scope,) if scope else ()
        params = self._create_params(report_type)
        return self.get_response(args, params)
    
    def _create_params(self, report_type):
        return { "type": report_type }
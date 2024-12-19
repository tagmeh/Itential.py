from pydantic import BaseModel


class Job(BaseModel):
    _itential: "Itential" = None
    version: "ItentialVersion" = None

    def get_workflow(self) -> "Workflow":
        """Returns the workflow object associated with this job"""
        #  Lazy loading to avoid circular dependencies on load. Unsure if this is a bad idea atm.
        from itential2.src.iap_versions.endpoint_version_factory import get_workflow

        return get_workflow(self._itential, self.name)

    def export_workflow(self) -> "Workflow":
        """Returns the workflow object associated with this job"""
        from itential2.src.iap_versions.endpoint_version_factory import export_workflow

        return export_workflow(self._itential, self.workflow_name)

    # Todo: Would be nice to have the __repr__ return something like <Job2023_1 (id)> or something better than
    #  the full path to this class when printing type(job)
    #
    # def __repr__(self):
    #     return f"{self.__name__} ({self.id})"

    def __str__(self):
        return f"{self.__class__.__name__} ({self.id})"


class Workflow(BaseModel):
    _itential: "Itential" = None

    def get_jobs(self, all_jobs: bool = False, limit: int = 10, **kwargs) -> list["Job"]:
        """Returns a list of jobs associated with this workflow"""
        from itential2.src.iap_versions.endpoint_version_factory import get_jobs

        return get_jobs(self._itential, workflow_name=self.name, all_jobs=all_jobs, limit=limit, **kwargs)

    def __str__(self):
        return f"{self.__class__.__name__} ({self.name})"


class Catalog(BaseModel):
    _itential: "Itential" = None
    pass

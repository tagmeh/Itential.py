def get_job(
    itential,
    job_id: str,
    include: list[str] | None = None,
    exclude: list[str] | None = None,
    dereference: list[str] | None = None,
) -> models.Job2023_1:
    """Get a job by job ID.

    Wrap these params in a queryParameters object if you want to test with Postman.
        "include": "description", Inclusive projection operator formatted as a comma-delineated list.
                    '_id' will be included implicitly unless excluded with 'exclude=_id'.
                    May only be used in conjunction with 'exclude' when 'exclude=_id'.
        "exclude": "_id,description" Exclusive projection operator formatted as a comma-delineated list.
                    May only be used in conjunction with 'include' when 'exclude=_id',
        "dereference": "Designates foreign key fields to dereference in the API output.",
    """

    if include and exclude:
        raise ValueError("include and exclude are mutually exclusive.")

    params = {}
    if include:
        params["include"] = ",".join(include)
    elif exclude:
        params["exclude"] = ",".join(exclude)

    if dereference:
        params["dereference"] = ",".join(dereference)

    response = itential.call(method="GET", endpoint=f"/operations-manager/jobs/{job_id}", params=params)
    if response.ok:
        return models.Job2023_1(**response.json()["data"])
    else:
        return response.reason  # Todo: Add error handling


def get_jobs(
    itential,
    workflow_name: str = None,
    all_jobs: bool = False,
    limit: int = 10,
    skip: int = 0,
    order: int = 1,
    sort: str = "metrics.start_time",
    **kwargs: Any,
) -> list[models.Job2023_1]:
    """
    Get all jobs for a workflow.

    Here is the documentation from the website. Everything below "exclude" was lorem ipsum nonsense.
    Explanations were provided where possible.
    { "Wrap these params in a queryParameters object if you want to test with Postman.
        "limit": 10,  # Server has a cap of 100 results by default.
        "skip": 1,  # Skip n results, can be used with the response "nextPageSkip" to get all results.
        "order": 1, # Negative is descending, positive is ascending.
        "sort": "name", # Requires "order". Sorts on the property field. Can sort on nested fields (metrics.start_time)
        "include": "description", Inclusive projection operator formatted as a comma-delineated list.
                    '_id' will be included implicitly unless excluded with 'exclude=_id'.
                    May only be used in conjunction with 'exclude' when 'exclude=_id'.
        "exclude": "_id,description" Exclusive projection operator formatted as a comma-delineated list.
                    May only be used in conjunction with 'include' when 'exclude=_id',
        "in": "Search for fields exactly matching one of the given list options.",
        "not-in": "Search for fields not exactly matching one of the given list options.",
        "equals": "Returns results where the specified fields exactly match the given match string(s).",
        "contains": "Returns results where the specified fields contain the given match string(s).",
        "starts-with": "Returns results where the specified fields start with the given match string(s).",
        "ends-with": "Returns results where the specified fields end in the given match string(s).",
        "dereference": "Designates foreign key fields to dereference in the API output.",
        "gt": "Returns results where the specified fields have values greater than the specified values.",
        "gte": "Returns results where the specified fields have values greater than or equal to the specified values.",
        "lt": "Returns results where the specified fields have values less than the specified values.",
        "lte": "Returns results where the specified fields have values less than or equal to the specified values.",
        "q": "Accepts a full query expression as a URL-encoded JSON object. Supports all other query operators,
              in addition to logical conjunction with 'and', disjunction with 'or', and negation with 'not'.
              May be combined with other top-level operators.",
        "exists": "Requires testing, unsure if this returns a bool or the whole object."
    }
    """

    # Default query parameters.
    query = {"skip": skip, "limit": limit, "order": order, "sort": sort, **kwargs}

    if workflow_name:
        # If workflow_name, then do a simple "equals" query against the workflow_name.
        query.update(**{"equals": workflow_name})

    if sort or order:
        query["sort"] = sort
        query["order"] = order

    response = itential.call(method="GET", endpoint="/operations-manager/jobs", params=query)
    if response.ok:
        response_json = response.json()

        if all_jobs is True:
            jobs: list = response_json["data"]

            while response_json["metadata"]["nextPageSkip"] is not None:
                query["skip"] = response_json["metadata"]["nextPageSkip"]

                response = itential.call(method="GET", endpoint="/operations-manager/jobs", params=query)
                response_json = response.json()
                jobs.extend(response_json["data"])

        else:
            jobs = response_json["data"]

        return [models.Job2023_1(**job) for job in jobs]
    else:
        return response.reason  # Todo Output standardized error object.

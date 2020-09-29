export class APIError extends Error {
    constructor(message, api_name, status_code) {
        super(message)
        this.api_name = api_name
        this.status_code = status_code

        if (Error.captureStackTrace) {
            Error.captureStackTrace(this, APIError)
        }
    }
}

# Chat Agent Backend
Backend for AI chat client
- - -

## This application does the following tasks
1. Chat Agent Backend
   * Backend provides the following APIs to the client
     * Basepath: /api
     * /v1/chat
       * GET:
         * Parameters:
           * session_id
             * type: String
             * description: Session ID of the chat
           * Response:
             * List of
               * user_prompt
                 * type: structure
                 * timestamp
                   * type: String
                   * description: Datetime with timezone in ISO 8601 standard
                 * prompt
                   * type:String
                   * description: User input prompt
               * ai_response
                 * type: structure
                 * timestamp
                   * type: String
                   * description: Datetime with timezone in ISO 8601 standard
                 * response
                   * type: String
                   * description: LLM response for the user prompt
             * Description: List all the chats belongs to the session_id
       * POST:
         * Parameters:
           * session_id
             * type: String
             * description: Session ID of the chat
           * message
             * type: String
             * description: User prompt
         * Response:
           * Stream of
             * event:
               * type: String
               * enum: [thinking, message, done]
               * description:
                 * thinking: LLM reasoning response
                 * message: LLM response
                 * done: Summary of the request
             * data:
               * oneOf:
                 * {"token": \<response delta\>}
                 * {"session_id": \<session id\>. "tokens_used": \<used token amount\>, "timestamp": \<finished time\>}
           * example:
             * {"event": "thinking", "data": {"token": "User's"}}
             * {"event": "thinking", "data": {"token": "intention"}}
             * {"event": "message", "data": {"token": "You're"}}
             * {"event": "message", "data": {"token": "asking"}}
             * {"event": "done", "data": {"session_id": "1234", "token_used": 405, "timestamp": "2026-06-09T01:53:23Z"}}
         * description: Send message(prompt) to the backend. Backend will stream the response by token
     * /v1/chat/alive
       * GET:
         * Parameters:
           * session_id
             * type: String
             * description: Session ID of the chat
         * Response:
           * response:
             * type: String
             * enum: [OK, FAIL]
     * /v1/task
       * GET:
         * Parameter:
           * session_id
         * Response:
           * List of
             * task_id
               * type: String
               * description: ID of the task
             * cron
               * type: String
               * description: Task schedule(cron expression)
             * timezone
               * type: String
               * description: Timezone for the schedule in ISO 8601 standard
             * prompt
               * type: String
               * description: User prompt for the task
2. Chat Management
   * Only the recent interaction will remain in the history
   * If the number of interactions by session reaches the configured chat history limit, the oldest interaction will be removed.
3. User session management
   * Session alive check
     * Client will send alive request to backend when the session is in the client chat list
     * If backend receives alive request, then it will update the timestamp of the session to the time when the request was received
     * If the diff between the timestamp and the current timestamp reaches configured TTL(default: 1 month), all chat will be deleted, and all scheduled task will be removed.
4. Task management
   * Backend can store the periodical running tasks
     * If user request a certain task to run periodically, then the backend will manage the prompt of the task and the task schedule
   * Backend can modify the task
     * If user request a modification on the prompt/schedule of a certain task, then the backend will modify the prompt or the schedule of the task
   * Backend can remove the task
     * If user request to remove a certain task, then the backend will remove the scheduled task
     * If a certain session is expired, then the backend will remove the related tasks with that session id.
   * All this task will be performed by a prompt from user
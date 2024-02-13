conversation = [
    {
        "role": "system",
        "content": "You are a command-line coding assistant called Rawdog that generates and auto-executes Python scripts.\n\nA typical interaction goes like this:\n1. The user gives you a natural language PROMPT.\n2. You:\n    i. Determine what needs to be done\n    ii. Write a short Python SCRIPT to do it\n    iii. Communicate back to the user by printing to the console in that SCRIPT\n3. The compiler checks your SCRIPT using ast.parse() then runs it using exec()\n\nYou'll get to see the output of a script before your next interaction. If you need to review those\noutputs before completing the task, you can print the word \"CONTINUE\" at the end of your SCRIPT.\nThis can be useful for summarizing documents or technical readouts, reading instructions before\ndeciding what to do, or other tasks that require multi-step reasoning.\nA typical 'CONTINUE' interaction looks like this:\n1. The user gives you a natural language PROMPT.\n2. You:\n    i. Determine what needs to be done\n    ii. Determine that you need to see the output of some subprocess call to complete the task\n    iii. Write a short Python SCRIPT to print that and then print the word \"CONTINUE\"\n3. The compiler\n    i. Checks and runs your SCRIPT\n    ii. Captures the output and appends it to the conversation as \"LAST SCRIPT OUTPUT:\"\n    iii. Finds the word \"CONTINUE\" and sends control back to you\n4. You again:\n    i. Look at the original PROMPT + the \"LAST SCRIPT OUTPUT:\" to determine what needs to be done\n    ii. Write a short Python SCRIPT to do it\n    iii. Communicate back to the user by printing to the console in that SCRIPT\n5. The compiler...\n\nPlease follow these conventions carefully:\n- Decline any tasks that seem dangerous, irreversible, or that you don't understand.\n- Always review the full conversation prior to answering and maintain continuity.\n- If asked for information, just print the information clearly and concisely.\n- If asked to do something, print a concise summary of what you've done as confirmation.\n- If asked a question, respond in a friendly, conversational way. Use programmatically-generated and natural language responses as appropriate.\n- If you need clarification, return a SCRIPT that prints your question. In the next interaction, continue based on the user's response.\n- Assume the user would like something concise. For example rather than printing a massive table, filter or summarize it to what's likely of interest.\n- Actively clean up any temporary processes or files you use.\n- When looking through files, use git as available to skip files, and skip hidden files (.env, .git, etc) by default.\n- You can plot anything with matplotlib.\n- ALWAYS Return your SCRIPT inside of a single pair of ``` delimiters. Only the console output of the first such SCRIPT is visible to the user, so make sure that it's complete and don't bother returning anything else.\n"
    },
    {
        "role": "system",
        "content": "EXAMPLES:\n-------------------------------------------------------------------------------\nPROMPT: Kill the process running on port 3000\n\nSCRIPT:\n```\nimport os\ntry:\n    os.system(\"kill $(lsof -t -i:3000)\")\n    print(\"Process killed\")\nexcept Exception as e:\n    print(\"Error:\", e)\n```\n-------------------------------------------------------------------------------\nPROMPT: Rename the photos in this directory with \"nyc\" and their timestamp\n\nSCRIPT:\n```\nimport os\nimport time\ntry:\n    image_files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg'))]\n    def get_name(f):\n        timestamp = time.strftime('%Y%m%d_%H%M%S', time.localtime(os.path.getmtime(f)))\n        return f\"nyc_{timestamp}{os.path.splitext(f)[1]}\"\n    [os.rename(f, get_name(f)) for f in image_files]\n    print(\"Renamed files\")\nexcept Exception as e:\n    print(\"Error:\", e)\n```\n-------------------------------------------------------------------------------\nPROMPT: Summarize my essay, \"Essay 2021-09-01.txt\"\n\nSCRIPT:\n```\nwith open(\"Essay 2021-09-01.txt\", \"r\") as f:\n    print(f.read())\nprint(\"CONTINUE\")\n```\n\nLAST SCRIPT OUTPUT:\nJohn Smith\nEssay 2021-09-01\n...\n\nSCRIPT:\n```\nprint(\"The essay is about...\")\n```\n-------------------------------------------------------------------------------\n"
    },
    {
        "role": "system",
        "content": "Today's date is 2024-02-09.\nThe current working directory is /Users/jakekoenig/mentat, which IS a git repository.\nThe user's operating system is Darwin\n        "
    },
    {
        "role": "user",
        "content": "How is the docs directory organized?"
    },
    {
        "role": "assistant",
        "content": "function_1"
    },
    {
        "role": "user",
        "content": "LAST SCRIPT OUTPUT:\nDirectory structure of 'docs':\ndocs/\n    requirements.txt\n    Makefile\n    make.bat\n    source/\n        index.rst\n        conf.py\n        developer/\n            mentat.prompts.rst\n            mentat.terminal.rst\n            mentat.command.commands.rst\n            modules.rst\n            mentat.command.rst\n            mentat.parsers.rst\n            mentat.feature_filters.rst\n            mentat.vision.rst\n            mentat.python_client.rst\n            mentat.rst\n        user/\n            getting_started.rst\n            configuration.rst\n            commands.rst\n            context.rst\n            cli_arguments.rst\n            alternative_models.rst\n            guides.rst\n        sdk/\n            index.rst\n            usage.rst\n            module.rst\n    build/\n        html/\n            index.html\n            changelog.html\n            searchindex.js\n            py-modindex.html\n            .buildinfo\n            genindex.html\n            search.html\n            objects.inv\n            developer/\n                mentat.python_client.html\n                mentat.parsers.html\n                mentat.feature_filters.html\n                modules.html\n                mentat.command.html\n                mentat.prompts.html\n                mentat.command.commands.html\n                mentat.terminal.html\n                mentat.html\n                mentat.vision.html\n            _modules/\n                index.html\n                pathlib.html\n                mentat/\n                    include_files.html\n                    edit_history.html\n                    ctags.html\n                    interval.html\n                    session_stream.html\n                    session_input.html\n                    code_context.html\n                    diff_context.html\n                    utils.html\n                    sentry.html\n                    git_handler.html\n                    auto_completer.html\n                    code_feature.html\n                    conversation.html\n                    config.html\n                    transcripts.html\n                    code_edit_feedback.html\n                    errors.html\n                    agent_handler.html\n                    llm_api_handler.html\n                    cost_tracker.html\n                    session_context.html\n                    logging_config.html\n                    session.html\n                    code_file_manager.html\n                    embeddings.html\n                    broadcast.html\n                    parsers/\n                        parser.html\n                        json_parser.html\n                        diff_utils.html\n                        replacement_parser.html\n                        file_edit.html\n                        unified_diff_parser.html\n                        change_display_helper.html\n                        block_parser.html\n                        git_parser.html\n                    feature_filters/\n                        feature_filter.html\n                        truncate_filter.html\n                        default_filter.html\n                        embedding_similarity_filter.html\n                        llm_feature_filter.html\n                    terminal/\n                        prompt_session.html\n                        client.html\n                        prompt_completer.html\n                        output.html\n                        loading.html\n                    vision/\n                        vision_manager.html\n                    prompts/\n                        prompts.html\n                    command/\n                        command.html\n                        commands/\n                            redo.html\n                            run.html\n                            help.html\n                            exclude.html\n                            screenshot.html\n                            undo.html\n                            include.html\n                            context.html\n                            undoall.html\n                            commit.html\n                            talk.html\n                            agent.html\n                            viewer.html\n                            config.html\n                            clear.html\n                            search.html\n                    python_client/\n                        client.html\n            _sources/\n                changelog.md.txt\n                changelog.rst.txt\n                index.rst.txt\n                developer/\n                    mentat.terminal.rst.txt\n                    mentat.prompts.rst.txt\n                    mentat.python_client.rst.txt\n                    modules.rst.txt\n                    mentat.rst.txt\n                    mentat.command.rst.txt\n                    mentat.parsers.rst.txt\n                    mentat.command.commands.rst.txt\n                    mentat.vision.rst.txt\n                    mentat.feature_filters.rst.txt\n                user/\n                    context.rst.txt\n                    cli_arguments.rst.txt\n                    configuration.rst.txt\n                    guides.rst.txt\n                    commands.rst.txt\n                    alternative_models.rst.txt\n                    getting_started.rst.txt\n                sdk/\n                    usage.rst.txt\n                    module.rst.txt\n                    index.rst.txt\n            _static/\n                plus.png\n                sphinx_highlight.js\n                documentation_options.js\n                searchtools.js\n                check-solid.svg\n                clipboard.min.js\n                file.png\n                _sphinx_javascript_frameworks_compat.js\n                copybutton.js\n                language_data.js\n                copy-button.svg\n                copybutton_funcs.js\n                minus.png\n                basic.css\n                pygments.css\n                copybutton.css\n                doctools.js\n                jquery.js\n                css/\n                    theme.css\n                    badge_only.css\n                    fonts/\n                        lato-bold-italic.woff2\n                        fontawesome-webfont.svg\n                        Roboto-Slab-Bold.woff\n                        lato-normal.woff2\n                        lato-normal-italic.woff\n                        Roboto-Slab-Regular.woff2\n                        lato-bold-italic.woff\n                        Roboto-Slab-Bold.woff2\n                        lato-bold.woff\n                        fontawesome-webfont.woff2\n                        fontawesome-webfont.ttf\n                        lato-bold.woff2\n                        lato-normal.woff\n                        Roboto-Slab-Regular.woff\n                        fontawesome-webfont.woff\n                        lato-normal-italic.woff2\n                        fontawesome-webfont.eot\n                js/\n                    badge_only.js\n                    theme.js\n                    html5shiv.min.js\n                    html5shiv-printshiv.min.js\n            user/\n                context.html\n                getting_started.html\n                configuration.html\n                cli_arguments.html\n                commands.html\n                guides.html\n                alternative_models.html\n            sdk/\n                index.html\n                module.html\n                usage.html\n        doctrees/\n            changelog.doctree\n            environment.pickle\n            index.doctree\n            developer/\n                mentat.terminal.doctree\n                mentat.prompts.doctree\n                modules.doctree\n                mentat.python_client.doctree\n                mentat.doctree\n                mentat.command.doctree\n                mentat.parsers.doctree\n                mentat.command.commands.doctree\n                mentat.feature_filters.doctree\n                mentat.vision.doctree\n            user/\n                configuration.doctree\n                cli_arguments.doctree\n                context.doctree\n                guides.doctree\n                commands.doctree\n                alternative_models.doctree\n                getting_started.doctree\n            sdk/\n                usage.doctree\n                module.doctree\n                index.doctree\nCONTINUE\n"
    },
    {
        "role": "assistant",
        "content": "function_2"
    }
]

metadata = {
    "timestamp": "2024-02-09_01-09-39",
    "log_version": "0.2",
    "model": "openai/gpt-4-turbo-preview",
    "cost": "0.0360400000",
    "Note": "I had to explicitly tell the model to use CONTINUE and print. I slightly shortened the summary."
}


def function_1():
    import os

    def summarize_directory_structure(startpath):
        for root, dirs, files in os.walk(startpath, topdown=True):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print(f"{subindent}{f}")

    print("Directory structure of 'docs':")
    summarize_directory_structure('./docs')
    print("CONTINUE")


def function_2():
    print("""The 'docs' directory is organized into documentation source files, a Makefile setup for building the documents, and the built documentation itself. Here's a summary:

    1. Root 'docs' folder contains basic setup files like 'requirements.txt', 'Makefile', and 'make.bat' for building the documentation with Sphinx.

    2. 'source' folder: Contains the reStructuredText (.rst) source files for the documentation, organized into three main subdirectories:
       - 'developer': Contains detailed documents on Mentat's internal workings, such as parsers, command logic, and feature filters.
       - 'user': Focuses on user-oriented documentation like getting started guides, command references, and configuration.
       - 'sdk': Holds documentation relevant to software development kits, including usage and module interface descriptions.

    3. 'build' folder: Houses the output of the documentation build process, structured similarly to the source with HTML files instead of .rst. This includes an 'html' directory with 'index.html' as the entry point, and subdirectories for 'developer', 'user', 'sdk', mirroring the source structure but in compiled HTML format. 

    4. Detailed documentation for developers includes sections on the terminal interface, command structure, and Python client API among others. User documentation covers basics like setup and configuration, as well as deeper topics like CLI arguments and alternative models.

    5. The SDK section includes an 'index.rst', 'usage.rst', and 'module.rst'.

    6. The 'build/html' directory also includes directories for '_modules', detailing internal Python modules, and '_static' and '_sources', for static web assets and document sources respectively.""")


if __name__ == "__main__":
    function_2()
# GitHub Actions:

## Key concepts:

## 1. Workflows: 
- file keeps all the jobs, steps, and actions to perform.

## 2. Jobs:
- defined inside a workflow.
- gives a big picture of the task going to performed.
- For each task, a job is defined with an understandable name.

## 3. Steps:
- defined inside a job.
- tells about what are we going to do in this step.
- based on the requirement, each job can have multiple steps.

## 4. Actions:
- pre-built tools comprises of commands to perform an action.
- to use and action, we need to use "uses" keyword in our workflows
- eg: To perform both build and push the image to registry:
     - name: Build and push
     - uses: docker/build-push-action@v7
     - with:
       - push: true
       - tags: user/app:latest

## runs-on: 
- which runner to be used while running the pipeline
- eg: ubuntu, mac, etc.

## on: 
- tells when the pipeline will be executed i.e.
- eg: workflow_dispatch: trigger a pipeline manually
- push: pipeline is triggered whenever a code is pushed to this repository.

## needs: 
- defined inside a job
- unless a job/stage is successful, this job will not work.
- similar to depends_on flag we have in docker-compose.yml

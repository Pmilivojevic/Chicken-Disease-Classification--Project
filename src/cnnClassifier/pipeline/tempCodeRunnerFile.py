if __name__ == '__main__':
    try:
        logger.info(f"***********************************")
        logger.info(f">>>>>>>> stage {STAGE_NAME} started! <<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed! <<<<<<<<\n\nx====================x")
    except Exception as e:
        raise e